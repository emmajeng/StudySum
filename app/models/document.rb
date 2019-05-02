class Document < ActiveRecord::Base
   has_one_attached :file
   
   # relationship
   has_one :user
end
