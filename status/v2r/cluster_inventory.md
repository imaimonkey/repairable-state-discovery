# V2R cluster inventory

2026-09-27T02:15:45.259614+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315160051712 available bytes; 82.42% used; 112443335 free inodes.

server1 `/home`: 315160051712 available bytes; 82.42% used; 112443335 free inodes.

server1 `/tmp`: 315160051712 available bytes; 82.42% used; 112443335 free inodes.

server1 `/var/tmp`: 315160051712 available bytes; 82.42% used; 112443335 free inodes.

server1 `/mnt/raid5`: 637261463552 available bytes; 97.08% used; 337401673 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17627176960 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17627176960 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17627176960 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17627176960 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 581382000640 available bytes; 95.98% used; 444885058 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78710599680 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78710599680 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1337723224064 available bytes; 81.51% used; 225762544 free inodes.

server3 `/tmp`: 78710599680 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78710599680 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105810309120 available bytes; 94.10% used; 114347750 free inodes.

server4 `/home`: 105810309120 available bytes; 94.10% used; 114347750 free inodes.

server4 `/data`: 400402284544 available bytes; 94.47% used; 224781838 free inodes.

server4 `/tmp`: 105810309120 available bytes; 94.10% used; 114347750 free inodes.

server4 `/var/tmp`: 105810309120 available bytes; 94.10% used; 114347750 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
