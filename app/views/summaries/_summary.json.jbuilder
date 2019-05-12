json.extract! summary, :id, :title, :body, :created_at, :updated_at
json.url summary_url(summary, format: :json)
