class Calculator {
    constructor() {
        this.value = 0;
        this.history = [];
    }

    add(number) {
        // basic addition
        let prev = this.value;
        this.value += number;
        return this.value;
    }

    subtract(number) {
        // basic subtraction
        this.value -= number;
        return this.value;
    }

    multiply(number) {
        // basic multiplication
        this.value *= number;
        return this.value;
    }

    divide(number) {
        // basic division
        if (number === 0) {
            console.error("Divide by zero");
            return null;
        }
        this.value /= number;
        return this.value;
    }
}

    power(number) {
        // basic exponentiation implementation
        this.value = Math.pow(this.value, number);
        return this.value;
    }
