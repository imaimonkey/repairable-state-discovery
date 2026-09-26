# V2R cluster inventory

2026-09-26T00:48:04.040263+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318649659392 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318649659392 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318649659392 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318649659392 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 345593499648 available bytes; 98.41% used; 337546757 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22932979712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22932979712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22932979712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22932979712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 294567915520 available bytes; 97.96% used; 445057272 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341514240 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84341514240 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124938727424 available bytes; 98.27% used; 225818743 free inodes.

server3 `/tmp`: 84341514240 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84341514240 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105349300224 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349300224 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148678307840 available bytes; 97.95% used; 224917384 free inodes.

server4 `/tmp`: 105349300224 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349300224 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
