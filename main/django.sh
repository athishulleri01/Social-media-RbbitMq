echo "Create migrations"
python3 manage.py makemigrations 
echo "=========================="

echo "Migrate"
python3 manage.py migrate 
echo "=========================="
