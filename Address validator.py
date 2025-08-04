import re

def validate_address(address):
    # Required fields
    required_fields = ["street", "city", "state", "zip"]
    missing_fields = [field for field in required_fields if field not in address]

    if missing_fields:
        return f"❌ Missing fields: {', '.join(missing_fields)}"

    # Validate ZIP (US ZIP or Indian PIN)
    zip_pattern_us = r"^\d{5}(-\d{4})?$"       # 12345 or 12345-6789
    zip_pattern_in = r"^\d{6}$"                # 600001

    if not (re.match(zip_pattern_us, address["zip"]) or re.match(zip_pattern_in, address["zip"])):
        return "❌ Invalid ZIP/PIN code format"

    # Validate state (Assume 2-letter code or full name alphabetic)
    if not address["state"].replace(" ", "").isalpha():
        return "❌ Invalid state format (should be alphabetic only)"

    # Everything looks fine
    return "✅ Address format is valid"

# Sample address dictionary
address_1 = {
    "street": "12, Gokul Street",
    "city": "Chennai",
    "state": "Tamil Nadu",
    "zip": "600001"
}

address_2 = {
    "street": "742 Evergreen Terrace",
    "city": "Springfield",
    "state": "IL",
    "zip": "62704"
}

address_3 = {
    "street": "No. 10, MG Road",
    "city": "Bangalore",
    "state": "KA",
    "zip": "5600A1"  # Invalid ZIP
}

# Run validations
print("Address 1:", validate_address(address_1))
print("Address 2:", validate_address(address_2))
print("Address 3:", validate_address(address_3))
