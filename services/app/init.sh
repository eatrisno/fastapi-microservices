_cdir=`pwd`
cd migrations
python3 migration.py

cd $_cdir/scripts
python3 init_db.py