# PatientRegistration.py

from queue import Queue

# Initialize queue for patient registration
patient_queue = Queue()

# Function to register patient
def register_patient(name):
    patient_queue.put(name)
    print(f"Patient {name} registered.")

# Function to remove patient after meeting doctor
def remove_patient():
    if not patient_queue.empty():
        removed_patient = patient_queue.get()
        print(f"Patient {removed_patient} removed after meeting the doctor.")
    else:
        print("No patients in the queue.")

# Function to display patient queue
def display_patient_queue():
    if not patient_queue.empty():
        print("Current patient queue:")
        for patient in patient_queue.queue:
            print(patient)
    else:
        print("No patients in the queue.")

# Main function
def main():
    while True:
        print("\n1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter patient name: ")
            register_patient(name)
        elif choice == "2":
            remove_patient()
        elif choice == "3":
            display_patient_queue()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
