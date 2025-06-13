#include <iostream>     // Standard I/O library
#include <cstring>      // For string operations
using namespace std;    // Avoid using std:: prefix repeatedly

// --------- STRUCT TO STORE STATIC MENU ITEMS ----------
struct MenuItem {
    char name[30];      // Name of the menu item (char array)
    float price;        // Price of the menu item
};

// Initialize static menu with 10 predefined items
MenuItem menu[20] = {
    {"Burger", 5.99},
    {"Fries", 2.49},
    {"Pizza", 8.99},
    {"Pasta", 7.50},
    {"Soda", 1.50},
    {"Coffee", 2.00},
    {"Salad", 4.25},
    {"Ice Cream", 3.75},
    {"Chicken Wings", 6.99},
    {"Steak", 12.99}
};

// --------- ABSTRACT BASE CLASS FOR ALL ORDERS ----------
class OrderBase {
public:
    MenuItem** selectedItems;  // Pointer to array of selected menu item pointers
    int itemCount;             // Number of items in the order

    virtual float totalCost() = 0;  // Pure virtual function to compute total
    virtual void printType() = 0;   // Abstract function to print order type

    // Virtual destructor to allow proper cleanup of derived objects
    virtual ~OrderBase() {
        delete[] selectedItems;     // Free selected items memory
    }
};

// --------- DINE-IN ORDER CLASS (DERIVED FROM OrderBase) ----------
class DineInOrder : public OrderBase {
public:
    float* serviceCharge;      // Dynamically allocated service charge

    // Constructor: takes charge, item array, and count
    DineInOrder(float charge, MenuItem** items, int count) {
        serviceCharge = new float(charge);          // Allocate service charge
        itemCount = count;                          // Set number of items
        selectedItems = new MenuItem*[count];       // Allocate selected items array
        for (int i = 0; i < count; i++) {
            selectedItems[i] = items[i];            // Copy item pointers
        }
    }

    // Override totalCost to add service charge
    float totalCost() override {
        float total = 0;
        for (int i = 0; i < itemCount; i++) {
            total += selectedItems[i]->price;       // Sum item prices
        }
        return total + *serviceCharge;              // Add service charge
    }

    // Print order type
    void printType() override {
        cout << "[Dine-In Order]" << endl;
    }

    // Destructor: free service charge
    ~DineInOrder() {
        delete serviceCharge;
    }
};

// --------- TAKE-OUT ORDER CLASS (DERIVED FROM OrderBase) ----------
class TakeOutOrder : public OrderBase {
public:
    float* packagingFee;       // Dynamically allocated packaging fee

    // Constructor: takes fee, item array, and count
    TakeOutOrder(float fee, MenuItem** items, int count) {
        packagingFee = new float(fee);              // Allocate packaging fee
        itemCount = count;                          // Set number of items
        selectedItems = new MenuItem*[count];       // Allocate selected items array
        for (int i = 0; i < count; i++) {
            selectedItems[i] = items[i];            // Copy item pointers
        }
    }

    // Override totalCost to add packaging fee
    float totalCost() override {
        float total = 0;
        for (int i = 0; i < itemCount; i++) {
            total += selectedItems[i]->price;       // Sum item prices
        }
        return total + *packagingFee;               // Add packaging fee
    }

    // Print order type
    void printType() override {
        cout << "[Take-Out Order]" << endl;
    }

    // Destructor: free packaging fee
    ~TakeOutOrder() {
        delete packagingFee;
    }
};

// --------- DYNAMIC ORDER MANAGEMENT SYSTEM ----------
OrderBase** orders = nullptr;   // Dynamic array of order pointers
int orderCount = 0;             // Total number of current orders

// Function to add an order to the list
void addOrder(OrderBase* newOrder) {
    OrderBase** temp = new OrderBase*[orderCount + 1]; // New larger array
    for (int i = 0; i < orderCount; i++) {
        temp[i] = orders[i];           // Copy existing orders
    }
    temp[orderCount] = newOrder;       // Add new order at the end
    delete[] orders;                   // Free old array
    orders = temp;                     // Update pointer to new array
    orderCount++;                      // Increment count
}

// Function to remove an order at a given index
void removeOrder(int index) {
    if (index < 0 || index >= orderCount) {
        cout << "Invalid order index." << endl;
        return; // Out of range check
    }

    delete orders[index]; // Delete the selected order object

    OrderBase** temp = new OrderBase*[orderCount - 1]; // Create smaller array
    for (int i = 0, j = 0; i < orderCount; i++) {
        if (i != index) {
            temp[j++] = orders[i];     // Copy all except the deleted one
        }
    }
    delete[] orders;                   // Delete old orders array
    orders = temp;                     // Update to new array
    orderCount--;                      // Decrement count
}

// --------- DISPLAY STATIC MENU ----------
void showMenu() {
    cout << "====== Restaurant Menu ======" << endl;
    for (int i = 0; i < 10; i++) {     // Show first 10 items
        cout << i << ". " << menu[i].name << " - $" << menu[i].price << endl;
    }
    cout << "=============================" << endl;
}

// --------- MAIN FUNCTION ----------
int main() {
    int choice; // Menu selection
    do {
        // Display main menu
        cout << "\n---- Restaurant Order System ----" << endl;
        cout << "1. Show Menu" << endl;
        cout << "2. Add Dine-In Order" << endl;
        cout << "3. Add Take-Out Order" << endl;
        cout << "4. View Orders" << endl;
        cout << "5. Remove Order" << endl;
        cout << "6. Exit" << endl;
        cout << "Choose: ";
        cin >> choice;

        // View menu
        if (choice == 1) {
            showMenu();
        }

        // Add Dine-In or Take-Out Order
        else if (choice == 2 || choice == 3) {
            int itemCount;
            cout << "How many items to order: ";
            cin >> itemCount;

            MenuItem** selected = new MenuItem*[itemCount]; // Create item array
            for (int i = 0; i < itemCount; i++) {
                int idx;
                showMenu(); // Show menu for each item selection
                cout << "Select item index #" << (i + 1) << ": ";
                cin >> idx;
                selected[i] = &menu[idx]; // Store pointer to menu item
            }

            // If Dine-In, ask for service charge
            if (choice == 2) {
                float serviceCharge;
                cout << "Enter service charge: ";
                cin >> serviceCharge;
                addOrder(new DineInOrder(serviceCharge, selected, itemCount));
            } 
            // If Take-Out, ask for packaging fee
            else {
                float packagingFee;
                cout << "Enter packaging fee: ";
                cin >> packagingFee;
                addOrder(new TakeOutOrder(packagingFee, selected, itemCount));
            }

            delete[] selected; // Clean up temporary item list
        }

        // View all orders
        else if (choice == 4) {
            if (orderCount == 0) {
                cout << "No orders yet!" << endl;
            } else {
                cout << "\n--- Orders Summary ---" << endl;
                for (int i = 0; i < orderCount; i++) {
                    cout << "Order #" << (i + 1) << ": ";
                    orders[i]->printType();                    // Display type
                    cout << "Total: $" << orders[i]->totalCost() << endl; // Display total
                    cout << "--------------------------" << endl;
                }
            }
        }

        // Remove an order
        else if (choice == 5) {
            int index;
            cout << "Enter order number to remove (1-based index): ";
            cin >> index;
            removeOrder(index - 1); // Convert to 0-based
        }

        // Exit
        else if (choice == 6) {
            cout << "Exiting..." << endl;
        }

        // Invalid choice handling
        else {
            cout << "Invalid choice. Try again." << endl;
        }

    } while (choice != 6); // Repeat until exit selected

    // Cleanup: delete all remaining orders
    for (int i = 0; i < orderCount; i++) {
        delete orders[i];
    }
    delete[] orders;

    return 0; // Exit the program
}
