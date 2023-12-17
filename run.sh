python3 generate_report.py
echo "Generated report!"
python3 build_site.py
echo "Built site!"
netlify deploy --dir=build --prod