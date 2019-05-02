class Document < ActiveRecord::Base
   has_one_attached :file
end
