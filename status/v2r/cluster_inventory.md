# V2R cluster inventory

2026-09-27T13:03:15.378658+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304674390016 available bytes; 83.00% used; 112401388 free inodes.

server1 `/home`: 304674390016 available bytes; 83.00% used; 112401388 free inodes.

server1 `/tmp`: 304674390016 available bytes; 83.00% used; 112401388 free inodes.

server1 `/var/tmp`: 304674390016 available bytes; 83.00% used; 112401388 free inodes.

server1 `/mnt/raid5`: 634593456128 available bytes; 97.09% used; 337424232 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13413699584 available bytes; 99.25% used; 110351845 free inodes.

server2 `/home`: 13413699584 available bytes; 99.25% used; 110351845 free inodes.

server2 `/tmp`: 13413699584 available bytes; 99.25% used; 110351845 free inodes.

server2 `/var/tmp`: 13413699584 available bytes; 99.25% used; 110351845 free inodes.

server2 `/mnt/raid5`: 529422811136 available bytes; 96.34% used; 444734196 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78576889856 available bytes; 95.62% used; 114062842 free inodes.

server3 `/home`: 78576889856 available bytes; 95.62% used; 114062842 free inodes.

server3 `/data`: 1331507539968 available bytes; 81.60% used; 225757876 free inodes.

server3 `/tmp`: 78576889856 available bytes; 95.62% used; 114062842 free inodes.

server3 `/var/tmp`: 78576889856 available bytes; 95.62% used; 114062842 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111011090432 available bytes; 93.81% used; 114372802 free inodes.

server4 `/home`: 111011090432 available bytes; 93.81% used; 114372802 free inodes.

server4 `/data`: 351724843008 available bytes; 95.14% used; 224727824 free inodes.

server4 `/tmp`: 111011090432 available bytes; 93.81% used; 114372802 free inodes.

server4 `/var/tmp`: 111011090432 available bytes; 93.81% used; 114372802 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
