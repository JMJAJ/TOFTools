from datetime import datetime, timedelta

def ticks_to_datetime(ticks):
    dotnet_epoch = datetime(1, 1, 1)
    microseconds = ticks // 10  # Convert ticks to microseconds
    return dotnet_epoch + timedelta(microseconds=microseconds)

def datetime_to_ticks(dt):
    dotnet_epoch = datetime(1, 1, 1)
    delta = dt - dotnet_epoch
    ticks = delta.total_seconds() * 10_000_000
    return int(ticks)

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Convert .NET ticks to datetime")
        print("2. Convert datetime to .NET ticks")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            ticks = input("Enter .NET ticks: ")
            try:
                ticks = int(ticks)
                dt = ticks_to_datetime(ticks)
                print(f"Corresponding datetime: {dt}")
            except ValueError:
                print("Invalid input. Please enter a valid integer for ticks.")
        
        elif choice == '2':
            date_string = input("Enter datetime (YYYY-MM-DD HH:MM:SS.ffffff): ")
            try:
                dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
                ticks = datetime_to_ticks(dt)
                print(f"Corresponding .NET ticks: {ticks}")
            except ValueError:
                print("Invalid datetime format. Please use YYYY-MM-DD HH:MM:SS.ffffff")
        
        elif choice == '3':
            print("Exiting the program..")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()