# V2R cluster inventory

2026-09-25T22:43:17.821976+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692782080 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318692782080 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318692782080 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318692782080 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 360215355392 available bytes; 98.35% used; 337538874 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952493056 available bytes; 98.72% used; 110406234 free inodes.

server2 `/home`: 22952493056 available bytes; 98.72% used; 110406234 free inodes.

server2 `/tmp`: 22952493056 available bytes; 98.72% used; 110406234 free inodes.

server2 `/var/tmp`: 22952493056 available bytes; 98.72% used; 110406234 free inodes.

server2 `/mnt/raid5`: 298588205056 available bytes; 97.94% used; 445052518 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351307776 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84351307776 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124824608768 available bytes; 98.27% used; 225805715 free inodes.

server3 `/tmp`: 84351307776 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84351307776 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235636224 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235636224 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192235687936 available bytes; 97.34% used; 224917689 free inodes.

server4 `/tmp`: 105235636224 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235636224 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
