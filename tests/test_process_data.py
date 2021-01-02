from pathlib import Path
from datetime import datetime
COLUMN_COUNT = 17


def decimal_latitude(lat: str) -> float:
    return float(lat[:2]) + float(lat[2:4]) / 60 + float(lat[4:]) / 60


def decimal_longitude(lon: str) -> float:
    return float(lon[:3]) + float(lon[3:5]) / 60 + float(lon[5:]) / 60


def test_load_raw_data():
    path = Path(__file__).parent / 'data.log'
    path_write = Path(__file__).parent / 'data.csv'
    with path.open() as fp:
        with path_write.open('w') as fw:
            fw.write('timestamp,lat,lon,speed,direction\n')
            for line in fp.readlines():
                cols = line.strip().split(': ')
                if len(cols) != 2:
                    continue
                r = cols[1].strip("b'").strip("#'").split(',')
                if len(r) != COLUMN_COUNT:
                    continue

                # Convert to standardized values
                id, time, str_lat, str_lon, speed_knots, direction, date = r[1], r[3], r[5], r[7], r[9], r[10], r[11]
                try:
                    timestamp = datetime.strptime(date+time, '%d%m%y%H%M%S')
                except ValueError:
                    # print(f'Could not parse: {line}')
                    pass
                lat = decimal_latitude(str_lat)
                lon = decimal_longitude(str_lon)
                speed_kmh = float(speed_knots) * 1.852
                # print(f'{timestamp} - {lat:.8f} N {lon:.8f} E {speed_kmh:.2f} km/h, {direction} az deg')
                fw.write(f'{timestamp},{lat:.8f},{lon:.8f},{speed_kmh:.4f},{direction}\n')
