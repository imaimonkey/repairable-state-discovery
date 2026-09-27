# V2R cluster inventory

2026-09-27T09:23:48.637279+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314451062784 available bytes; 82.46% used; 112440730 free inodes.

server1 `/home`: 314451062784 available bytes; 82.46% used; 112440730 free inodes.

server1 `/tmp`: 314451062784 available bytes; 82.46% used; 112440730 free inodes.

server1 `/var/tmp`: 314451062784 available bytes; 82.46% used; 112440730 free inodes.

server1 `/mnt/raid5`: 635457900544 available bytes; 97.08% used; 337424509 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16515067904 available bytes; 99.08% used; 110356966 free inodes.

server2 `/home`: 16515067904 available bytes; 99.08% used; 110356966 free inodes.

server2 `/tmp`: 16515067904 available bytes; 99.08% used; 110356966 free inodes.

server2 `/var/tmp`: 16515067904 available bytes; 99.08% used; 110356966 free inodes.

server2 `/mnt/raid5`: 573867802624 available bytes; 96.03% used; 444742004 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78557696000 available bytes; 95.62% used; 114062917 free inodes.

server3 `/home`: 78557696000 available bytes; 95.62% used; 114062917 free inodes.

server3 `/data`: 1332519415808 available bytes; 81.58% used; 225762532 free inodes.

server3 `/tmp`: 78557696000 available bytes; 95.62% used; 114062917 free inodes.

server3 `/var/tmp`: 78557696000 available bytes; 95.62% used; 114062917 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050530816 available bytes; 93.80% used; 114372843 free inodes.

server4 `/home`: 111050530816 available bytes; 93.80% used; 114372843 free inodes.

server4 `/data`: 364100890624 available bytes; 94.97% used; 224767435 free inodes.

server4 `/tmp`: 111050530816 available bytes; 93.80% used; 114372843 free inodes.

server4 `/var/tmp`: 111050530816 available bytes; 93.80% used; 114372843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
