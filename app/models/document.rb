class Document < ActiveRecord::Base
   has_one_attached :file
   
   def file_path
     ActiveStorage::Blob.service.path_for(file.key)
   end
   
   # relationship
   has_one :user
end
