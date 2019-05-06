json.extract! input, :id, :title, :body, :created_at, :updated_at
json.url input_url(input, format: :json)
