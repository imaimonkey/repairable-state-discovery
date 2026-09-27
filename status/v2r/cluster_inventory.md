# V2R cluster inventory

2026-09-27T12:49:32.266385+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304681984000 available bytes; 83.00% used; 112401389 free inodes.

server1 `/home`: 304681984000 available bytes; 83.00% used; 112401389 free inodes.

server1 `/tmp`: 304681984000 available bytes; 83.00% used; 112401389 free inodes.

server1 `/var/tmp`: 304681984000 available bytes; 83.00% used; 112401389 free inodes.

server1 `/mnt/raid5`: 634599149568 available bytes; 97.09% used; 337424230 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13422854144 available bytes; 99.25% used; 110352069 free inodes.

server2 `/home`: 13422854144 available bytes; 99.25% used; 110352069 free inodes.

server2 `/tmp`: 13422854144 available bytes; 99.25% used; 110352069 free inodes.

server2 `/var/tmp`: 13422854144 available bytes; 99.25% used; 110352069 free inodes.

server2 `/mnt/raid5`: 548338741248 available bytes; 96.21% used; 444734686 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78577356800 available bytes; 95.62% used; 114062861 free inodes.

server3 `/home`: 78577356800 available bytes; 95.62% used; 114062861 free inodes.

server3 `/data`: 1331523203072 available bytes; 81.60% used; 225758052 free inodes.

server3 `/tmp`: 78577356800 available bytes; 95.62% used; 114062861 free inodes.

server3 `/var/tmp`: 78577356800 available bytes; 95.62% used; 114062861 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111011401728 available bytes; 93.81% used; 114372802 free inodes.

server4 `/home`: 111011401728 available bytes; 93.81% used; 114372802 free inodes.

server4 `/data`: 351926956032 available bytes; 95.14% used; 224727837 free inodes.

server4 `/tmp`: 111011401728 available bytes; 93.81% used; 114372802 free inodes.

server4 `/var/tmp`: 111011401728 available bytes; 93.81% used; 114372802 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
