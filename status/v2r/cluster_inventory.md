# V2R cluster inventory

2026-09-23T20:09:19.975633+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325740572672 available bytes; 81.83% used; 112501841 free inodes.

server1 `/home`: 325740572672 available bytes; 81.83% used; 112501841 free inodes.

server1 `/tmp`: 325740572672 available bytes; 81.83% used; 112501841 free inodes.

server1 `/var/tmp`: 325740572672 available bytes; 81.83% used; 112501841 free inodes.

server1 `/mnt/raid5`: 1388308029440 available bytes; 93.63% used; 337741126 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41271115776 available bytes; 97.70% used; 110434859 free inodes.

server2 `/home`: 41271115776 available bytes; 97.70% used; 110434859 free inodes.

server2 `/tmp`: 41271115776 available bytes; 97.70% used; 110434859 free inodes.

server2 `/var/tmp`: 41271115776 available bytes; 97.70% used; 110434859 free inodes.

server2 `/mnt/raid5`: 541546356736 available bytes; 96.26% used; 445211387 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293275480064 available bytes; 83.63% used; 114224185 free inodes.

server3 `/home`: 293275480064 available bytes; 83.63% used; 114224185 free inodes.

server3 `/data`: 52616388608 available bytes; 99.27% used; 225844148 free inodes.

server3 `/tmp`: 293275480064 available bytes; 83.63% used; 114224185 free inodes.

server3 `/var/tmp`: 293275480064 available bytes; 83.63% used; 114224185 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106528755712 available bytes; 94.06% used; 114356232 free inodes.

server4 `/home`: 106528755712 available bytes; 94.06% used; 114356232 free inodes.

server4 `/data`: 1024000 available bytes; 100.00% used; 225457630 free inodes.

server4 `/tmp`: 106528755712 available bytes; 94.06% used; 114356232 free inodes.

server4 `/var/tmp`: 106528755712 available bytes; 94.06% used; 114356232 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
