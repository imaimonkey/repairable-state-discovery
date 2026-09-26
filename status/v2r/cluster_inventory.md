# V2R cluster inventory

2026-09-26T01:40:32.193624+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318649733120 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318649733120 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318649733120 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318649733120 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 345476812800 available bytes; 98.42% used; 337546448 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940168192 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22940168192 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22940168192 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22940168192 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 290402775040 available bytes; 97.99% used; 445055465 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339265536 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84339265536 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124796657664 available bytes; 98.28% used; 225817829 free inodes.

server3 `/tmp`: 84339265536 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84339265536 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196658688 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196658688 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 131412938752 available bytes; 98.18% used; 224915912 free inodes.

server4 `/tmp`: 105196658688 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196658688 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
