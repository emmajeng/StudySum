class Profile < ActiveRecord::Base
  belongs_to :user
  has_one_attached :image
  
  
end
