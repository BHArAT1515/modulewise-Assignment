try {
    let num = 10;
    let result = num / 0;
    if (!isFinite(result)) {
        throw new Error("Cannot divide by zero!");
    }
    console.log(result);
} catch (error) {
    console.log("Error:", error.message);
}
