```mermaid
classDiagram
    class CoffeeShop {
        +string name
        +sellCoffee() void
    }

    class Customer {
        +string name
        +buyCoffee(CoffeeShop shop) void
    }

    Customer --> CoffeeShop : buys from
```