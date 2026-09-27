# V2R cluster inventory

2026-09-27T02:29:27.691632+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315078840320 available bytes; 82.42% used; 112443393 free inodes.

server1 `/home`: 315078840320 available bytes; 82.42% used; 112443393 free inodes.

server1 `/tmp`: 315078840320 available bytes; 82.42% used; 112443393 free inodes.

server1 `/var/tmp`: 315078840320 available bytes; 82.42% used; 112443393 free inodes.

server1 `/mnt/raid5`: 637263089664 available bytes; 97.08% used; 337401648 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17634435072 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17634435072 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17634435072 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17634435072 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 580992294912 available bytes; 95.99% used; 444884799 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78709620736 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78709620736 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1337686425600 available bytes; 81.51% used; 225762363 free inodes.

server3 `/tmp`: 78709620736 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78709620736 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111036403712 available bytes; 93.80% used; 114373252 free inodes.

server4 `/home`: 111036403712 available bytes; 93.80% used; 114373252 free inodes.

server4 `/data`: 400295665664 available bytes; 94.47% used; 224781590 free inodes.

server4 `/tmp`: 111036403712 available bytes; 93.80% used; 114373252 free inodes.

server4 `/var/tmp`: 111036403712 available bytes; 93.80% used; 114373252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
