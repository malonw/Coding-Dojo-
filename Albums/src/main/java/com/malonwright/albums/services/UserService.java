package com.malonwright.albums.services;

import java.util.List;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.malonwright.albums.models.User;
import com.malonwright.albums.repositories.UserRepository;

@Service
public class UserService {
	@Autowired
	private UserRepository uRepo;
	
	public List<User> getAllUsers(){
		return this.uRepo.findAll();
	}
	
	public User getOneUser(Long id) {
		return this.uRepo.findById(id).orElse(null);
	}
	public User registerUser(User user) {
		//Generate the hash
		String hashed = BCrypt.hashpw(user.getpassword(), BCrypt.gensalt());
		//Set the hashed password on the users password field
		user.setPassword(hashed);
		//Save that user and user object to the db
		return this.uRepo.save(user);
	}
	public boolean authenticateUser(String email, String password) {
//		Query the user by email
		User user = this.uRepo.findByEmail(email);
		if(user == null) {
			return false;
		}
//	}cjecl [rpvoded e,ao; agaomst db
		retutn BCrypt.checkpw(password, user.getPassword());
}
	public User getUserByEmail(String email) {
		return this.uRepo.
	}
}