class Calculator {
    constructor() {
        this.value = 0;
        this.history = [];
    }

    add(number) {
        // advanced addition with type check
        if (typeof number !== 'number') {
            throw new Error("Input must be a valid number");
        }
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
        // strict division handling
        if (number === 0) {
            throw new Error("ArithmeticException: Divide by zero");
        }
        this.value = this.value / number;
        return this.value;
    }
}

    power(number) {
        // basic exponentiation implementation
        this.value = Math.pow(this.value, number);
        return this.value;
    }

    squareRoot() {
        // calculate square root
        if (this.value < 0) return null;
        this.value = Math.sqrt(this.value);
        return this.value;
    }

    inverse() {
        // calculate mathematical inverse
        if (this.value === 0) throw new Error("Zero inverse");
        this.value = 1 / this.value;
        return this.value;
    }
