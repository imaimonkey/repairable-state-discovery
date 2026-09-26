# V2R cluster inventory

2026-09-26T07:52:00.574157+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318754463744 available bytes; 82.22% used; 112476267 free inodes.

server1 `/home`: 318754463744 available bytes; 82.22% used; 112476267 free inodes.

server1 `/tmp`: 318754463744 available bytes; 82.22% used; 112476267 free inodes.

server1 `/var/tmp`: 318754463744 available bytes; 82.22% used; 112476267 free inodes.

server1 `/mnt/raid5`: 219187220480 available bytes; 98.99% used; 337539131 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22320857088 available bytes; 98.75% used; 110403907 free inodes.

server2 `/home`: 22320857088 available bytes; 98.75% used; 110403907 free inodes.

server2 `/tmp`: 22320857088 available bytes; 98.75% used; 110403907 free inodes.

server2 `/var/tmp`: 22320857088 available bytes; 98.75% used; 110403907 free inodes.

server2 `/mnt/raid5`: 270620704768 available bytes; 98.13% used; 445026196 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82680143872 available bytes; 95.39% used; 114110865 free inodes.

server3 `/home`: 82680143872 available bytes; 95.39% used; 114110865 free inodes.

server3 `/data`: 123902214144 available bytes; 98.29% used; 225820671 free inodes.

server3 `/tmp`: 82680143872 available bytes; 95.39% used; 114110865 free inodes.

server3 `/var/tmp`: 82680143872 available bytes; 95.39% used; 114110865 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106073792512 available bytes; 94.08% used; 114348161 free inodes.

server4 `/home`: 106073792512 available bytes; 94.08% used; 114348161 free inodes.

server4 `/data`: 105676587008 available bytes; 98.54% used; 224922515 free inodes.

server4 `/tmp`: 106073792512 available bytes; 94.08% used; 114348161 free inodes.

server4 `/var/tmp`: 106073792512 available bytes; 94.08% used; 114348161 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
