class Calculator {
    constructor() {
        this.value = 0;
        this.history = [];
    }

    add(number) {
        // addition with history tracking
        const oldVal = this.value;
        this.value += number;
        this.history.push({ op: 'add', val: number });
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

    modulo(number) {
        // basic modulo operation logic
        if (number === 0) return null;
        this.value = this.value % number;
        return this.value;
    }

    factorial() {
        // calculate factorial recursively or iteratively
        if (this.value < 0 || !Number.isInteger(this.value)) return null;
        let result = 1;
        for (let i = 2; i <= this.value; i++) result *= i;
        this.value = result;
        return this.value;
    }
