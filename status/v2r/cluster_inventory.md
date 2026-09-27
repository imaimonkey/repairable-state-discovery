# V2R cluster inventory

2026-09-27T12:44:56.859724+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304683405312 available bytes; 83.00% used; 112401394 free inodes.

server1 `/home`: 304683405312 available bytes; 83.00% used; 112401394 free inodes.

server1 `/tmp`: 304683405312 available bytes; 83.00% used; 112401394 free inodes.

server1 `/var/tmp`: 304683405312 available bytes; 83.00% used; 112401394 free inodes.

server1 `/mnt/raid5`: 634591346688 available bytes; 97.09% used; 337424230 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13425229824 available bytes; 99.25% used; 110352069 free inodes.

server2 `/home`: 13425229824 available bytes; 99.25% used; 110352069 free inodes.

server2 `/tmp`: 13425229824 available bytes; 99.25% used; 110352069 free inodes.

server2 `/var/tmp`: 13425229824 available bytes; 99.25% used; 110352069 free inodes.

server2 `/mnt/raid5`: 548457979904 available bytes; 96.21% used; 444734632 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78577905664 available bytes; 95.62% used; 114062861 free inodes.

server3 `/home`: 78577905664 available bytes; 95.62% used; 114062861 free inodes.

server3 `/data`: 1331746324480 available bytes; 81.59% used; 225758131 free inodes.

server3 `/tmp`: 78577905664 available bytes; 95.62% used; 114062861 free inodes.

server3 `/var/tmp`: 78577905664 available bytes; 95.62% used; 114062861 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111011504128 available bytes; 93.81% used; 114372805 free inodes.

server4 `/home`: 111011504128 available bytes; 93.81% used; 114372805 free inodes.

server4 `/data`: 352033546240 available bytes; 95.13% used; 224727837 free inodes.

server4 `/tmp`: 111011504128 available bytes; 93.81% used; 114372805 free inodes.

server4 `/var/tmp`: 111011504128 available bytes; 93.81% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
