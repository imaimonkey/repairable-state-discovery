# V2R cluster inventory

2026-09-26T00:36:23.153476+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318651727872 available bytes; 82.22% used; 112476300 free inodes.

server1 `/home`: 318651727872 available bytes; 82.22% used; 112476300 free inodes.

server1 `/tmp`: 318651727872 available bytes; 82.22% used; 112476300 free inodes.

server1 `/var/tmp`: 318651727872 available bytes; 82.22% used; 112476300 free inodes.

server1 `/mnt/raid5`: 345621860352 available bytes; 98.41% used; 337546812 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942552064 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22942552064 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22942552064 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22942552064 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 294894931968 available bytes; 97.96% used; 445057504 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342222848 available bytes; 95.29% used; 114152441 free inodes.

server3 `/home`: 84342222848 available bytes; 95.29% used; 114152441 free inodes.

server3 `/data`: 124943478784 available bytes; 98.27% used; 225818942 free inodes.

server3 `/tmp`: 84342222848 available bytes; 95.29% used; 114152441 free inodes.

server3 `/var/tmp`: 84342222848 available bytes; 95.29% used; 114152441 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349611520 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349611520 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148735729664 available bytes; 97.94% used; 224917403 free inodes.

server4 `/tmp`: 105349611520 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349611520 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
