# V2R cluster inventory

2026-09-24T03:43:42.940770+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324741570560 available bytes; 81.88% used; 112493740 free inodes.

server1 `/home`: 324741570560 available bytes; 81.88% used; 112493740 free inodes.

server1 `/tmp`: 324741570560 available bytes; 81.88% used; 112493740 free inodes.

server1 `/var/tmp`: 324741570560 available bytes; 81.88% used; 112493740 free inodes.

server1 `/mnt/raid5`: 402124173312 available bytes; 98.16% used; 337724835 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40827629568 available bytes; 97.72% used; 110430997 free inodes.

server2 `/home`: 40827629568 available bytes; 97.72% used; 110430997 free inodes.

server2 `/tmp`: 40827629568 available bytes; 97.72% used; 110430997 free inodes.

server2 `/var/tmp`: 40827629568 available bytes; 97.72% used; 110430997 free inodes.

server2 `/mnt/raid5`: 526800605184 available bytes; 96.36% used; 445197505 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291974533120 available bytes; 83.71% used; 114174949 free inodes.

server3 `/home`: 291974533120 available bytes; 83.71% used; 114174949 free inodes.

server3 `/data`: 33883234304 available bytes; 99.53% used; 225842718 free inodes.

server3 `/tmp`: 291974533120 available bytes; 83.71% used; 114174949 free inodes.

server3 `/var/tmp`: 291974533120 available bytes; 83.71% used; 114174949 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105792897024 available bytes; 94.10% used; 114349570 free inodes.

server4 `/home`: 105792897024 available bytes; 94.10% used; 114349570 free inodes.

server4 `/data`: 277723168768 available bytes; 96.16% used; 225384301 free inodes.

server4 `/tmp`: 105792897024 available bytes; 94.10% used; 114349570 free inodes.

server4 `/var/tmp`: 105792897024 available bytes; 94.10% used; 114349570 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
