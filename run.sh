echo "Generating report..."
python3 generate_report.py
echo "Done!"

echo "Building site..."
python3 build_site.py
echo "Done!"

echo "Deploying..."
python3 netlify_upload.py
echo "Done!"