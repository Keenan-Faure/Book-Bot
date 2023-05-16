const { crawlPage } = require('./crawl.js');
const { printReport } = require('./printReport.js');

async function main()
{
    if((process.argv).length > 3)
    {
        console.log("Too many arguments");
        process.exit();
    }
    else if((process.argv).length < 3)
    {
        console.log("Too few arguments");
        process.exit();
    }
    else if((process.argv).length == 3)
    {
        let argument = process.argv[2];
        console.log("Starting the crawler application at " + argument);
        result = await crawlPage(argument, argument, {});
        printReport(result);
    }
}
main()