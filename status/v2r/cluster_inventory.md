# V2R cluster inventory

2026-09-24T16:17:45.267077+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025204736 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324025204736 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324025204736 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324025204736 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416597696512 available bytes; 98.09% used; 337654816 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57335889920 available bytes; 96.80% used; 110427011 free inodes.

server2 `/home`: 57335889920 available bytes; 96.80% used; 110427011 free inodes.

server2 `/tmp`: 57335889920 available bytes; 96.80% used; 110427011 free inodes.

server2 `/var/tmp`: 57335889920 available bytes; 96.80% used; 110427011 free inodes.

server2 `/mnt/raid5`: 501341007872 available bytes; 96.54% used; 445165061 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84332339200 available bytes; 95.29% used; 114154568 free inodes.

server3 `/home`: 84332339200 available bytes; 95.29% used; 114154568 free inodes.

server3 `/data`: 159791755264 available bytes; 97.79% used; 225797476 free inodes.

server3 `/tmp`: 84332339200 available bytes; 95.29% used; 114154568 free inodes.

server3 `/var/tmp`: 84332339200 available bytes; 95.29% used; 114154568 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697501184 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697501184 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89292341248 available bytes; 98.77% used; 225255976 free inodes.

server4 `/tmp`: 105697501184 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697501184 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
