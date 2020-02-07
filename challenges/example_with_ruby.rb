## Example with Ruby for test the `BackEnd` Application

require "net/http"
require "json"


# Number of repositories using `Python`
puts "# Number of repositories using `Python`"
url = URI("http://localhost:8000/api/number/?language=Python")
response = Net::HTTP.get_response(url)
if response.code == '200'
  puts JSON(response.body)
else
  puts "Not found !!"
end

# List of repositories using `Python`
puts "\n# List of repositories using `Python`"
url = URI("http://localhost:8000/api/list/?language=Python")
response = Net::HTTP.get_response(url)
if response.code == '200'
  puts JSON(response.body)
else
  puts "Not found !!"
end

# `Python` popularity
puts "\n# `Python` popularity"
url = URI("http://localhost:8000/api/popularity/?language=Python")
response = Net::HTTP.get_response(url)
if response.code == '200'
  puts JSON(response.body)
else
  puts "Not found !!"
end
