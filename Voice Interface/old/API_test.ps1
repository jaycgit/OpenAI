Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process


# Set your API key
$apiKey = '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'  # Replace with your actual API key

# Define the API endpoint
$apiEndpoint = 'https://api.openai.com/v1/engines/davinci/completions'

# Define the prompt text
$promptText = 'Translate the following English text to French: "Hello, world!"'

# Create the request body
$requestBody = @{
    prompt = $promptText
    max_tokens = 50  # Adjust as needed
}

# Convert the request body to JSON
$jsonBody = $requestBody | ConvertTo-Json

# Set up the headers
$headers = @{
    'Authorization' = "Bearer $apiKey"
    'Content-Type' = 'application/json'
}

# Make the API call
$response = Invoke-RestMethod -Uri $apiEndpoint -Method Post -Headers $headers -Body $jsonBody

Write-Host "This is some output."
Write-Output "Another piece of output."

# Display the API response
$response | Format-Table -AutoSize

#

