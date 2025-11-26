#!/bin/bash

# Delete entities from Home Assistant entity registry
# Usage: ./delete_entities.sh entity_id1 entity_id2 entity_id3 ...
# Example: ./delete_entities.sh sensor.old_sensor switch.unused_switch

REGISTRY_FILE="/mnt/cache/appdata/homeassistant/.storage/core.entity_registry"
BACKUP_FILE="${REGISTRY_FILE}.backup.$(date +%Y%m%d_%H%M%S)"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed"
    echo "Install it with: apt-get install jq (or your package manager)"
    exit 1
fi

# Check if running as root or with appropriate permissions
if [ ! -w "$REGISTRY_FILE" ]; then
    echo "Error: Cannot write to $REGISTRY_FILE"
    echo "Please run this script with appropriate permissions (e.g., as root or homeassistant user)"
    exit 1
fi

# Check if entity IDs were provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 entity_id1 [entity_id2 entity_id3 ...]"
    echo ""
    echo "Example: $0 sensor.old_sensor switch.unused_switch"
    echo ""
    echo "This script will:"
    echo "  1. Create a backup of the entity registry"
    echo "  2. Remove the specified entities from the registry"
    echo "  3. Provide instructions to restart Home Assistant"
    exit 1
fi

# Check if registry file exists
if [ ! -f "$REGISTRY_FILE" ]; then
    echo "Error: Registry file not found at $REGISTRY_FILE"
    exit 1
fi

# Create backup
echo "Creating backup: $BACKUP_FILE"
cp "$REGISTRY_FILE" "$BACKUP_FILE"

if [ $? -ne 0 ]; then
    echo "Error: Failed to create backup"
    exit 1
fi

echo "Backup created successfully"
echo ""

# Process each entity ID
ENTITIES_TO_DELETE=("$@")
echo "Entities to delete:"
for entity_id in "${ENTITIES_TO_DELETE[@]}"; do
    echo "  - $entity_id"
done
echo ""

# Get original count
ORIGINAL_COUNT=$(jq '.data.entities | length' "$REGISTRY_FILE")

# Track results
DELETED=()
NOT_FOUND=()

# Check which entities exist
for entity_id in "${ENTITIES_TO_DELETE[@]}"; do
    EXISTS=$(jq --arg id "$entity_id" '.data.entities | any(.entity_id == $id)' "$REGISTRY_FILE")
    if [ "$EXISTS" = "true" ]; then
        DELETED+=("$entity_id")
    else
        NOT_FOUND+=("$entity_id")
    fi
done

# Build jq filter to remove all entities at once
if [ ${#DELETED[@]} -gt 0 ]; then
    # Create a JSON array of entity IDs to delete
    DELETE_ARRAY=$(printf '%s\n' "${DELETED[@]}" | jq -R . | jq -s .)

    # Use jq to filter out the entities
    jq --argjson ids "$DELETE_ARRAY" \
       '.data.entities |= map(select(.entity_id as $eid | $ids | index($eid) | not))' \
       "$REGISTRY_FILE" > "${REGISTRY_FILE}.tmp"

    if [ $? -eq 0 ]; then
        mv "${REGISTRY_FILE}.tmp" "$REGISTRY_FILE"
    else
        echo "Error: jq processing failed"
        rm -f "${REGISTRY_FILE}.tmp"
        echo "Restoring from backup..."
        cp "$BACKUP_FILE" "$REGISTRY_FILE"
        echo "Backup restored"
        exit 1
    fi
fi

# Get new count
NEW_COUNT=$(jq '.data.entities | length' "$REGISTRY_FILE")

# Print results
echo "Original entity count: $ORIGINAL_COUNT"
echo "New entity count: $NEW_COUNT"
echo "Deleted: ${#DELETED[@]} entities"
echo ""

if [ ${#DELETED[@]} -gt 0 ]; then
    echo "Successfully deleted:"
    for entity_id in "${DELETED[@]}"; do
        echo "  ✓ $entity_id"
    done
    echo ""
fi

if [ ${#NOT_FOUND[@]} -gt 0 ]; then
    echo "Not found in registry:"
    for entity_id in "${NOT_FOUND[@]}"; do
        echo "  ✗ $entity_id"
    done
    echo ""
fi

if [ ${#DELETED[@]} -gt 0 ]; then
    echo "✓ Entities deleted successfully"
    echo ""
    echo "Next steps:"
    echo "  1. Restart Home Assistant container to apply changes"
    echo "  2. If something goes wrong, restore from backup:"
    echo "     cp $BACKUP_FILE $REGISTRY_FILE"
    exit 0
else
    echo "⚠ No entities were deleted"
    exit 0
fi

