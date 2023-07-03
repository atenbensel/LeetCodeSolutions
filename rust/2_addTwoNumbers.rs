/// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
/// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

/// Solution:

// Definition for singly-linked list.
// struct ListNode {
//     val: i32,
//     next: Option<Box<ListNode>>,
// }
// 
// impl ListNode {
//     #[inline]
//     fn new(val: i32) -> Self {
//         ListNode { val, next: None }
//     }
// }

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode::new(0)));
        let mut current = &mut dummy;
        let (mut p, mut q) = (l1, l2);
        let (mut carry, mut sum) = (0, 0);
        
        while p.is_some() || q.is_some() {
            sum = carry;
            
            if let Some(node) = p {
                sum += node.val;
                p = node.next;
            }
            
            if let Some(node) = q {
                sum += node.val;
                q = node.next;
            }
            
            carry = sum / 10;
            sum %= 10;
            
            if let Some(node) = current {
                node.next = Some(Box::new(ListNode::new(sum)));
                current = &mut node.next;
            }
        }
        
        if carry > 0 {
            if let Some(node) = current {
                node.next = Some(Box::new(ListNode::new(carry)));
            }
        }
        
        dummy.unwrap().next
    }
}
