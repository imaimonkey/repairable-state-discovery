# V2R cluster inventory

2026-09-26T00:56:14.362344+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318659006464 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318659006464 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318659006464 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318659006464 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345571672064 available bytes; 98.41% used; 337546715 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931759104 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22931759104 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22931759104 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22931759104 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 293801828352 available bytes; 97.97% used; 445056900 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84337172480 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84337172480 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124935114752 available bytes; 98.27% used; 225818602 free inodes.

server3 `/tmp`: 84337172480 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84337172480 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349033984 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349033984 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148670672896 available bytes; 97.95% used; 224917354 free inodes.

server4 `/tmp`: 105349033984 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349033984 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
