# V2R cluster inventory

2026-09-24T07:10:55.468341+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324459745280 available bytes; 81.90% used; 112491265 free inodes.

server1 `/home`: 324459745280 available bytes; 81.90% used; 112491265 free inodes.

server1 `/tmp`: 324459745280 available bytes; 81.90% used; 112491265 free inodes.

server1 `/var/tmp`: 324459745280 available bytes; 81.90% used; 112491265 free inodes.

server1 `/mnt/raid5`: 517427716096 available bytes; 97.63% used; 337722824 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57861496832 available bytes; 96.77% used; 110431153 free inodes.

server2 `/home`: 57861496832 available bytes; 96.77% used; 110431153 free inodes.

server2 `/tmp`: 57861496832 available bytes; 96.77% used; 110431153 free inodes.

server2 `/var/tmp`: 57861496832 available bytes; 96.77% used; 110431153 free inodes.

server2 `/mnt/raid5`: 518328909824 available bytes; 96.42% used; 445181664 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127195852800 available bytes; 92.90% used; 114200124 free inodes.

server3 `/home`: 127195852800 available bytes; 92.90% used; 114200124 free inodes.

server3 `/data`: 139114934272 available bytes; 98.08% used; 225834528 free inodes.

server3 `/tmp`: 127195852800 available bytes; 92.90% used; 114200124 free inodes.

server3 `/var/tmp`: 127195852800 available bytes; 92.90% used; 114200124 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790038016 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790038016 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 296347127808 available bytes; 95.90% used; 225367386 free inodes.

server4 `/tmp`: 105790038016 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790038016 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
