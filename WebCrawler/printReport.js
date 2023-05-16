/**
 * Prints a report of the pages found
 * @param {Object} pages 
 */
function printReport(pages)
{
    console.log("----- Report is starting... -----");
    let sortable = sortObject(pages);
    for(const key in sortable)
    {
        console.log(`Found ${sortable[key]} internal links to ${key}`);
    }
    console.log("------- End of Report -------");
}

/**
 * Sorts the object in desc order
 * @param {Object} object 
 * @returns
 */
function sortObject(object)
{
    const sortable = Object.fromEntries(
        Object.entries(object).sort(([,a],[,b]) => b-a)
    );
    return sortable;
}

module.exports = {
    sortObject,
    printReport
}