// src/test/java/com/example/demo/controller/UserControllerTest.java
package com.example.demo.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(UserController.class)
public class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void testGetUser() throws Exception {
        mockMvc.perform(get("/api/users/123"))
                .andExpect(status().isOk())
                .andExpect(content().string("User with ID: 123"));
    }

    @Test
    public void testCreateUser() throws Exception {
        mockMvc.perform(post("/api/users")
                .param("name", "John"))
                .andExpect(status().isOk())
                .andExpect(content().string("Created user: John"));
    }
}