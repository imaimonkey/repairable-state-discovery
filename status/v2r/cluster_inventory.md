# V2R cluster inventory

2026-09-24T09:21:38.807939+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324463861760 available bytes; 81.90% used; 112489932 free inodes.

server1 `/home`: 324463861760 available bytes; 81.90% used; 112489932 free inodes.

server1 `/tmp`: 324463861760 available bytes; 81.90% used; 112489932 free inodes.

server1 `/var/tmp`: 324463861760 available bytes; 81.90% used; 112489932 free inodes.

server1 `/mnt/raid5`: 503190171648 available bytes; 97.69% used; 337714369 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57776132096 available bytes; 96.78% used; 110430838 free inodes.

server2 `/home`: 57776132096 available bytes; 96.78% used; 110430838 free inodes.

server2 `/tmp`: 57776132096 available bytes; 96.78% used; 110430838 free inodes.

server2 `/var/tmp`: 57776132096 available bytes; 96.78% used; 110430838 free inodes.

server2 `/mnt/raid5`: 514863190016 available bytes; 96.44% used; 445178045 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85861744640 available bytes; 95.21% used; 114199137 free inodes.

server3 `/home`: 85861744640 available bytes; 95.21% used; 114199137 free inodes.

server3 `/data`: 165863227392 available bytes; 97.71% used; 225821057 free inodes.

server3 `/tmp`: 85861744640 available bytes; 95.21% used; 114199137 free inodes.

server3 `/var/tmp`: 85861744640 available bytes; 95.21% used; 114199137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758076928 available bytes; 94.10% used; 114349051 free inodes.

server4 `/home`: 105758076928 available bytes; 94.10% used; 114349051 free inodes.

server4 `/data`: 257424814080 available bytes; 96.44% used; 225273310 free inodes.

server4 `/tmp`: 105758076928 available bytes; 94.10% used; 114349051 free inodes.

server4 `/var/tmp`: 105758076928 available bytes; 94.10% used; 114349051 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
