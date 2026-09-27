# V2R cluster inventory

2026-09-27T11:33:19.943186+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304695611392 available bytes; 83.00% used; 112401622 free inodes.

server1 `/home`: 304695611392 available bytes; 83.00% used; 112401622 free inodes.

server1 `/tmp`: 304695611392 available bytes; 83.00% used; 112401622 free inodes.

server1 `/var/tmp`: 304695611392 available bytes; 83.00% used; 112401622 free inodes.

server1 `/mnt/raid5`: 634682224640 available bytes; 97.09% used; 337424394 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16424689664 available bytes; 99.08% used; 110353091 free inodes.

server2 `/home`: 16424689664 available bytes; 99.08% used; 110353091 free inodes.

server2 `/tmp`: 16424689664 available bytes; 99.08% used; 110353091 free inodes.

server2 `/var/tmp`: 16424689664 available bytes; 99.08% used; 110353091 free inodes.

server2 `/mnt/raid5`: 570108387328 available bytes; 96.06% used; 444737133 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543118336 available bytes; 95.62% used; 114062811 free inodes.

server3 `/home`: 78543118336 available bytes; 95.62% used; 114062811 free inodes.

server3 `/data`: 1331929706496 available bytes; 81.59% used; 225759419 free inodes.

server3 `/tmp`: 78543118336 available bytes; 95.62% used; 114062811 free inodes.

server3 `/var/tmp`: 78543118336 available bytes; 95.62% used; 114062811 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111030095872 available bytes; 93.80% used; 114372814 free inodes.

server4 `/home`: 111030095872 available bytes; 93.80% used; 114372814 free inodes.

server4 `/data`: 353352601600 available bytes; 95.12% used; 224728125 free inodes.

server4 `/tmp`: 111030095872 available bytes; 93.80% used; 114372814 free inodes.

server4 `/var/tmp`: 111030095872 available bytes; 93.80% used; 114372814 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
