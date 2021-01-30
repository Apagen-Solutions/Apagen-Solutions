# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountBalanceCheck(models.TransientModel):
    _name = 'account.balance.check'
    _description = 'Wizard for checking account balance'

    account_id = fields.Many2one('account.account', 'Account', required=True)
    date = fields.Date('Date', required=True)
    check_bal = fields.Boolean('Check Balance', default=False)
    balance = fields.Float('Balance')

    @api.multi
    def check_balance(self):
        for wiz in self:
            domain = [('account_id', '=', wiz.account_id.id),
                      ('date', '<=', wiz.date)]
            move_lines = self.env['account.move.line'].search(domain)
            balance = 0
            for line in move_lines:
                balance += line.debit - line.credit
#             if balance < 0:
#                 print ('?????????????***********')
#                 balance = -balance
            wiz.balance = balance
            wiz.check_bal = True
            return {
                'view_mode': 'form',
                'res_id': wiz.id,
                'res_model': 'account.balance.check',
                'view_type': 'form',
                'type': 'ir.actions.act_window',
                'name': 'Account Balance Check',
                'context': self.env.context,
                'target': 'new',
            }
