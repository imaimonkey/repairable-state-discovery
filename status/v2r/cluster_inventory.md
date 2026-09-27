# V2R cluster inventory

2026-09-27T02:07:25.149878+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315161255936 available bytes; 82.42% used; 112443326 free inodes.

server1 `/home`: 315161255936 available bytes; 82.42% used; 112443326 free inodes.

server1 `/tmp`: 315161255936 available bytes; 82.42% used; 112443326 free inodes.

server1 `/var/tmp`: 315161255936 available bytes; 82.42% used; 112443326 free inodes.

server1 `/mnt/raid5`: 637478469632 available bytes; 97.08% used; 337405411 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17627729920 available bytes; 99.02% used; 110364994 free inodes.

server2 `/home`: 17627729920 available bytes; 99.02% used; 110364994 free inodes.

server2 `/tmp`: 17627729920 available bytes; 99.02% used; 110364994 free inodes.

server2 `/var/tmp`: 17627729920 available bytes; 99.02% used; 110364994 free inodes.

server2 `/mnt/raid5`: 581614952448 available bytes; 95.98% used; 444885421 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78714556416 available bytes; 95.61% used; 114062951 free inodes.

server3 `/home`: 78714556416 available bytes; 95.61% used; 114062951 free inodes.

server3 `/data`: 1338761035776 available bytes; 81.50% used; 225762627 free inodes.

server3 `/tmp`: 78714556416 available bytes; 95.61% used; 114062951 free inodes.

server3 `/var/tmp`: 78714556416 available bytes; 95.61% used; 114062951 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810579456 available bytes; 94.10% used; 114347759 free inodes.

server4 `/home`: 105810579456 available bytes; 94.10% used; 114347759 free inodes.

server4 `/data`: 403626270720 available bytes; 94.42% used; 224782022 free inodes.

server4 `/tmp`: 105810579456 available bytes; 94.10% used; 114347759 free inodes.

server4 `/var/tmp`: 105810579456 available bytes; 94.10% used; 114347759 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
