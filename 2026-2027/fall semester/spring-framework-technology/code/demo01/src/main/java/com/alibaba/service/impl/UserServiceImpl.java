package com.alibaba.service.impl;

import com.alibaba.service.UserService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class UserServiceImpl implements UserService {


    @Override
    public String getUserInfo() {
        return "zhangsan";
    }

    @Override
    public String getUserId(Long userId) {
        log.debug("userId:{}",userId);
        return String.valueOf(userId);
    }


}
