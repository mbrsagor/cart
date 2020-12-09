class Cart {
    constructor(name, product_name, price) {
        this.name = name;
        this.product_name = product_name;
        this.price = price;
    }

    all() {
        const config = `Car name is: ${this.name}\nProduct name:${this.product_name}\nPrice:${this.price}`;
        console.log(config);
    }
}

const my_car = new Cart('something', 'something 2', 129393);
my_car.all();

