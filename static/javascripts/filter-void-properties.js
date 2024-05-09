function filterVoidProperties(arrayOfProperties) {
    console.log(arrayOfProperties)
    const filtered = arrayOfProperties.filter((prop) => prop.void == true)
    return filtered
}