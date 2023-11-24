#!/bin/bash

# Create folder
folder="tests_data"

rm -rf "$folder"
mkdir -p "$folder"
echo "Folder created: $folder"

# Create test cases
input_1="tests_data/input_1.txt"
expected_1="tests_data/expected_1.txt"

input_2="tests_data/input_2.txt"
expected_2="tests_data/expected_2.txt"

cat <<EOF > "$input_1"
EOF

cat <<EOF > "$expected_1"
EOF


cat <<EOF > "$input_2"
EOF

cat <<EOF > "$expected_2"
EOF
