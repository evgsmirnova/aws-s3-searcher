<h2>AWS S3 Searcher</h2>
<p>The project makes it easy to search for files with a given extension in a specified AWS S3 bucket. A paginator is used for searching, allowing you to work with a large data, in case when there are more than 1000 objects. There is logging and a handler for the most common errors.</p>
<h3>Getting Started:</h3>
<ul>
  <li>Update credentials for the AWS S3 role where the required bucket is stored;</li>
  <li>In the configuration file <b>config.json</b> change the names for "bucket_name", "prefix_name" and "extension_name" to the ones you need;</li>
</ul>
<h3>Output: </h3>
<p>As a result, you will get the <b>result.txt</b> with a list of absolute paths to the found files on AWS. In the <b>app.log</b>, you can view the logs in case something went wrong.</p>